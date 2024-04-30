class DebugMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ", ".join([f"{attr}={getattr(self, attr)}" for attr in self.__dict__])
        return f"{class_name} ({attributes})"


