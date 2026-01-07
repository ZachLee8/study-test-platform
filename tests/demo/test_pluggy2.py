


from pluggy import PluginManager, HookspecMarker, HookimplMarker

pm = PluginManager('myproject')
hookspec = HookspecMarker('myproject')
hookimpl = HookimplMarker('myproject')



class Hookspecs:
    @hookspec
    def test_hook(self, arg1, arg2) -> None:
        """钩子规范，定义钩子函数的接口"""

class HookImpls:
    @hookimpl  
    def test_hook(self, arg1, arg2) -> None:
        """钩子实现，实现test_hook的功能"""
        print(f"lalallalla{arg1, arg2}")


# 注册钩子规范
pm.add_hookspecs(Hookspecs())
# 注册钩子实现
pm.register(HookImpls())
# 使用钩子
pm.hook.test_hook(arg1='a', arg2='b')