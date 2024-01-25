from core import Core

core = Core(id="123")

data={
    "About": {
        "zh": "关于"
    },
    "About the App": {
        "zh": "退出APP"
    },
    "Clear Context": {
        "zh": "清除所有上下文"
    }
}
core.update(data)
#core.add("test")
#print(core.get("About3","zh"))

core.add_lang("de")
#core.add_langs(["de","fr","nl"])
core.translate()
#core.delete_key("test")
#core.export_code_lang("py")
core.save()