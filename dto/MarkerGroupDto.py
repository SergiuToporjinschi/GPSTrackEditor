from .MarkerDto import MarkerDto, MarkerCategory

class MarkerGroupDto:
    category:MarkerCategory = None
    markers:list[MarkerDto] = []

    def __init__(self, category: MarkerCategory = None, markersList: list[MarkerDto] = None) -> None:
        self.category = category
        self.markers = markersList if markersList is not None else []
        pass
