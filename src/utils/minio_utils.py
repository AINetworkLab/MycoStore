import os
from ..services import model_save
from ..services import model_save_tf
from ..services import model_compose
from ..services import model_compose_tf
from minio import Minio
import heapq

def _save_state_dict(state_dict, path, type="torch", **kwargs):

    if not isinstance(state_dict, dict):
        raise TypeError(
            "Invalid object type for `state_dict`: {}. Must be an instance of `dict`".format(
                type(state_dict)
            )
        )
    
    os.makedirs(path, exist_ok=True)
    # state_dict_path = os.path.join(path, _TORCH_STATE_DICT_FILE_NAME)
    # torch.save(state_dict, state_dict_path, **kwargs)
    if type == "torch":
        return model_save.save_state_dict(dirs=path, state_dict=state_dict, **kwargs)
    elif type == "tensorflow":
        return model_save_tf.save_state_dict(dirs=path, state_dict=state_dict, **kwargs)
    # return model_save.save_state_dict(dirs=path, state_dict=state_dict, **kwargs)

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
    # 对磁盘空间按照剩余空间从大到小排序
    sorted_disks = sorted(disk_spaces.items(), key=lambda x: x[1], reverse=True)

    # 遍历排序后的磁盘空间，选择第一个剩余空间大于等于文件大小的磁盘
    for disk_key, free_space in sorted_disks:
        minio_id = disk_key.split("_")[0]  # 提取 minio_id 部分
        if int(free_space) >= file_size:
            return str(minio_id)
    
    # 如果所有磁盘的剩余空间都不足以存储文件，返回 -1
    return str(-1)

def load_layer(hash_set, base_path, type="torch"):
    if type == "torch":
        return model_compose(hash_set, base_path)
    elif type == "tensorflow":
        return model_compose_tf(hash_set, base_path)