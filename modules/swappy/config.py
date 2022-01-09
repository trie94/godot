def can_build(env, platform):
    return platform.startswith("android")  # only build for android


def configure(env):
    pass
