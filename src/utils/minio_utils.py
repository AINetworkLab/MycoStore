import os
from ..services import model_save
from ..services import model_save_tf
from ..services import model_compose
from ..services import model_compose_tf
from minio import Minio
import heapq
from collections import defaultdict

def _save_state_dict(state_dict, path, type="torch", **kwargs):

    if not isinstance(state_dict, dict):
        raise TypeError(
            "Invalid object type for `state_dict`: {}. Must be an instance of `dict`".format(
                type(state_dict)
            )
        )
    
    os.makedirs(path, exist_ok=True)
    if type == "torch":
        return model_save.save_state_dict(dirs=path, state_dict=state_dict, **kwargs)
    elif type == "tensorflow":
        return model_save_tf.save_state_dict(dirs=path, state_dict=state_dict, **kwargs)

def match_and_group(L_prime, k, group):
    for layer_id in L_prime:
        prefix = layer_id[:k]
        if prefix not in group:
            group[prefix] = [layer_id]
        else:
            matched = False
            for item in group[prefix]:
                if item == layer_id:
                    matched = True
                    break
            if not matched:
                group[prefix].append(layer_id)
    return group

def common_layer_identification(layer_hash_list, k=4, bucket=None):
    if bucket is None:
        bucket = defaultdict(list)
    # Intra-model
    local = defaultdict(list)
    local = match_and_group(layer_hash_list, k, local)
    all_local_layers = [layer_id for group in local.values() for layer_id in group]
    # Inter-model 
    bucket = match_and_group(all_local_layers, k, bucket)
    return bucket

def get_client(disk_id):
    if disk_id == "1":
        return Minio("localhost:9010",
            access_key="DJTaCd38KkiYyRtwQh5Q",
            secret_key="HjlJcGPFxCiDuXlRjbv2Eba0OCqYCz4IOFIDlxqU",
            secure=False
        )
    if disk_id == "2":
        return Minio("localhost:9020",
            access_key="4J2F73K7wtDrkdI7NpmH", 
            secret_key="s4vOXCyltOIW8jWm8B9bNl4qRtMkejw4CbBzsq6z",
            secure=False
        )
    if disk_id == "3":
        return Minio("localhost:9030",
            access_key="KPk1yeNUdDhncwjMBNXp", 
            secret_key="FdYvYVV74TDIDQmKcombFFwNZyUQT3gTjN9v0pHO",
            secure=False
        )
    if disk_id == "4":
        return Minio("localhost:9040",
            access_key="FFSka67zeuXfjPCZkkdc", 
            secret_key="hHs9lnHhurJvBXvn03DAYUrRufRWbHbYveX4lPal",
            secure=False
        )
    return None

def get_disk(file_size, disk_spaces):
    sorted_disks = sorted(disk_spaces.items(), key=lambda x: x[1], reverse=True)

    for disk_key, free_space in sorted_disks:
        minio_id = disk_key.split("_")[0]
        if int(free_space) >= file_size:
            return str(minio_id)
    
    return str(-1)

def load_layer(hash_set, base_path, type="torch"):
    if type == "torch":
        return model_compose(hash_set, base_path)
    elif type == "tensorflow":
        return model_compose_tf(hash_set, base_path)
