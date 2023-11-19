from geoalchemy2 import Geography, Geometry, Raster


def include_object(obj, name, obj_type, *args):
    if obj_type == "table" and (
        name.startswith("geometry_columns")
        or name.startswith("spatial_ref_sys")
        or name.startswith("spatialite_history")
        or name.startswith("sqlite_sequence")
        or name.startswith("views_geometry_columns")
        or name.startswith("virts_geometry_columns")
        or name.startswith("idx_")
    ):
        return False
    elif hasattr(obj, "schema") and obj.schema in ["tiger", "topology", "tiger_data"]:
        return False
    return True


def render_item(obj_type, obj, autogen_context):
    """Add proper imports for spatial types."""
    if obj_type == "type" and isinstance(obj, (Geometry, Geography, Raster)):
        import_name = obj.__class__.__name__
        autogen_context.imports.add(f"from geoalchemy2 import {import_name}")
        return "%r" % obj
    elif obj_type == "type" and obj.__class__.__module__.startswith(
        "sqlalchemy_utils."
    ):
        if hasattr(obj, "choices"):
            return f"{obj.__class__.__module__}.{obj.__class__.__name__}(choices={obj.choices})"
        else:
            return f"{obj.__class__.__module__}.{obj.__class__.__name__}()"

    # Default rendering for other objects
    return False
