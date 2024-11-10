import param

agus = param.Arg(
    params={
        "token" : {
            "flag" : "--t",
            "type" : int,
            "default" : 12,
        },
        "cipok" : {
            "flag" : "--c",
            "type" : str,
            "default" : None,
            "chaint" : "token"
        }
    }
)

print(agus.val("cipok"))
print(agus.all)