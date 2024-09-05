from urllib.parse import urlencode

def mapserver_query(url: str, **kwargs) -> str:
    """Query an ArcGIS MapServer.

    Refer to the ArcGIS API docs for supported query parameters:
    https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer/

    Arguments:
        url: URL path up to but not including the query. e.g:
            https://geo.abs.gov.au/arcgis/rest/services/ASGS2021/SA2/MapServer/0
        **kwargs: specify params as keyword arguments

    Returns:
        URL with query appended. e.g:
        https://geo.abs.gov.au/arcgis/rest/services/ASGS2021/SA2/MapServer/0/query?geometryType=esriGeometryEnvelope"

    Examples:

    >>> url = "https://geo.abs.gov.au/arcgis/rest/services/ASGS2021/SA2/MapServer/0"
    >>> mapserver_query(
    ...     url,
    ...     geometry="149.964039508913, -34.7693150002823, 151.075483568455, -33.8017423609583",
    ...     geometryType="esriGeometryEnvelope",
    ...     inSR=4326,
    ...     spatialRel="esriSpatialRelIntersects",
    ...     outFields="*",
    ...     returnGeometry="true",
    ...     featureEncoding="esriDefault",
    ...     f="geojson",
    ... )
    "https://geo.abs.gov.au/arcgis/rest/services/ASGS2021/SA2/MapServer/0/query?geometryType=esriGeometryEnvelope&outFields=%2A&returnGeometry=true&f=geojson&geometry=149.964039508913%2C+-34.7693150002823%2C+151.075483568455%2C+-33.8017423609583&inSR=4326&spatialRel=esriSpatialRelIntersects&featureEncoding=esriDefault"
    """

    default_params = {
        "geometryType": "esriGeometryEnvelope",
        "outFields": "*",
        "returnGeometry": "true",
        "f": "geojson",
    }

    params = default_params | params | kwargs

    return url + "/query?" + urlencode(params)
