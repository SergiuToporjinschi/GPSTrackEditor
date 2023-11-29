from .MarkerDto import MarkerDto

class MarkerGroupDto:
    category:str = None
    markers:list[MarkerDto] = []

    def __init__(self, category: str = None, markersList: list[MarkerDto] = None) -> None:
        self.category = category
        self.markers = markersList if markersList is not None else []
        pass
