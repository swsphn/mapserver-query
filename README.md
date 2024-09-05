# MapServer Query

This simple module allows you to easily generate query URLs for ArcGIS
MapServer APIs.

## Install

Install with your favourite package manager.
For example, install with pip:

    pip install https://github.com/swsphn/mapserver-query.git

## Use

Refer to the ArcGIS API docs for supported query parameters:  
https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer/

Arguments:  

-   `url`: URL path up to but not including the query. e.g:  
    https://geo.abs.gov.au/arcgis/rest/services/ASGS2021/SA2/MapServer/0
-   `**kwargs`: specify params as keyword arguments

Returns:  
    URL with query appended. e.g:  
    https://geo.abs.gov.au/arcgis/rest/services/ASGS2021/SA2/MapServer/0/query?geometryType=esriGeometryEnvelope

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

Once you have generated a query URL you can use it. For example, you can
open it in your browser to inspect the JSON data. Or you can pass it to
`requests.get()`, or `geopandas.read_file()` as required.
