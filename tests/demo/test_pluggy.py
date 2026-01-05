import pluggy


pm = pluggy.PluginManager('myproject')
hookspec = pluggy.HookspecMarker('myproject')
hookimpl = pluggy.HookimplMarker('myproject')


# 定义钩子规范（接口）
@hookspec
def test_hook(arg1, arg2):
    """钩子规范，定义钩子函数的接口"""
    pass


# @hookimpl
# def test_hook(arg1, arg2):
#     """钩子实现，实现test_hook的功能"""
#     print(f"lalallalla{arg1, arg2}")

class Plug:
    # 钩子实现
    @hookimpl
    def test_hook(self, arg1, arg2):
        """钩子实现，实现test_hook的功能"""
        print(f"lalallalla{arg1, arg2}")




# 注册钩子规范
pm.add_hookspecs(test_hook)
pm.register(Plug())
# 注册钩子实现
pm.hook.test_hook(arg1='a', arg2='b')