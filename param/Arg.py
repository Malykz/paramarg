import sys
import logging
import json


logger = logging.getLogger(__name__)

class Arg :
    """"
    [Decorator]
    run      :: Run function directly if param in command
    required :: Could'nt run the function if param not in command

    [staticMethod]
    get      :: return value of flag
    """

    def __init__(self, params:dict=None, command:list=sys.argv) :
        self.ARGUMEN = command
        self.PARAMS = params
        try : 
            self.allowed_flags = [val["flag"] for val in self.PARAMS.values()]
        except AttributeError :   
            self.allowed_flags = lambda : print("PARAMS is not denived")
            pass

        for name_param in self.PARAMS.keys() :
            self.__set_attr_param(name_param)    

    def run(self, condition, index=1) -> None :
        def wraper(f) :
            try :
                if self.ARGUMEN[index] == condition:
                    f()       
            except IndexError :
                self.__pass

        return wraper           

    def required(self, condition) :
        def wraper(f) :
            if condition in self.ARGUMEN :
                return f
            else :
                return self.__pass
        return wraper
                      
    def __pass(*a, **k) :
        pass

    @property
    def vals(self) -> dict :
        return self.__get_all_val([x for x in self.ARGUMEN if x in self.allowed_flags])    

    @property
    def all(self) -> dict :
        return self.__get_all_val(self.allowed_flags)   
    
    @property
    def __REQUIRED_KEY(self) :
        return ["flag", # Done
                "type", # Done
                "default", # Done
                "filter", 
                "description",
                "chaint",
                "from",
                "allias"]

    def val(self, name:dict, default=False) -> str | int:
        try : 
            default_val = (self.PARAMS[name]["default"]
                          if default == False 
                          else default)

            value = self._getval(
                self.PARAMS[name],
                default_val
            )

            self.__set_chaint(name)

            return self._getval(
                self.PARAMS[name], 
                default_val
            )

        except TypeError :
            raise TypeError("Error, PARAMS is not defined" )         

    def __get_all_val(self, flags:dict) -> dict :
        val = {}
        for flag in flags :
            param_attr = self.__search_param_attr_by_attr(flag)
            attr = param_attr[0]
            val.update({
                param_attr[1] : self._getval(attr, attr["default"])
            })
        return val         
    
    
    def __set_attr_param(self, param) :
        param_attr = self.PARAMS[param]
        yahaha = [x for x in self.__REQUIRED_KEY if x not in param_attr.keys()]
        for x in yahaha:
            param_attr.update({
                x : None
            })
        return param_attr        


    # Filter
    def __set_chaint(self, arg) :
        attr: str = self.PARAMS[arg]["chaint"]
        if attr != None and self.val(attr, "None") != "None":
            pass
        elif attr == None :
            pass    
        else :  
            logger.critical(f"{arg} requiring {attr}")
            sys.exit()



    # Fungi Bisa Banget Dipake Untuk JSNV
    def __search_param_attr_by_attr(self, attr) -> tuple : 
        for param in self.PARAMS.keys() :
            if attr in self.PARAMS[param].values() :
                return (self.PARAMS[param], param)
                 

    def _getval(self, param_attr, default) :
        dtype = param_attr["type"]

        if dtype == list :
            try :
                gblk = self.ARGUMEN[self.ARGUMEN.index(param_attr["flag"]) :] 
                try :
                    iyah = [
                            x for x in self.ARGUMEN
                            if x in self.allowed_flags and x in gblk and gblk[0] != x
                           ][0]
                except :
                    iyah = None    
                val = (
                      gblk[1 : gblk.index(iyah)]
                      if iyah != None
                      else gblk[1 :]
                )
                return (
                        default
                        if len(val) + 1 == 1
                        else val
                )
            except :
                return default 

        if dtype == bool :
            return (
                True 
                if param_attr["flag"] in self.ARGUMEN and param_attr["flag"] in self.allowed_flags 
                else default 
            )   

        try :
            flag = param_attr["flag"]
            if flag in self.ARGUMEN and flag in self.allowed_flags:
                val = self.ARGUMEN[self.ARGUMEN.index(flag) + 1]

                if val in self.allowed_flags :
                    return default
                
                try : 
                    return dtype(val
                                 if param_attr["type"] != "int" 
                                 else int(val))
                except :
                    logger.error(f"'{val}' must have {param_attr['type']} type")
                
            else :
                return default
            
        except IndexError :
            return default
        




