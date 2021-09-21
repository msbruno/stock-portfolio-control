

def path_resource(rel_path:str):
    import os
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, rel_path)
    