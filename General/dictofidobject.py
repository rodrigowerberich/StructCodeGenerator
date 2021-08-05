class DictOfIdObject:
    def __init__(self, objects_with_id):
        self._objects_with_id = {}
        for object_with_id in objects_with_id:
            self._objects_with_id[object_with_id.id] = object_with_id

    def __iter__(self):
        return self._objects_with_id.__iter__()

    def __getitem__(self, item):
        return self._objects_with_id.__getitem__(item)

    def __contains__(self, item):
        return self._objects_with_id.__contains__(item)