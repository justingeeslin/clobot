
from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
           
class CLOBot():

    @staticmethod
    def go(object):
        CLOBot.createGarmentsFromBlocks()
        CLOBot.createProjectsAndImagesFromGarments(object)

    @staticmethod
    def createGarmentsFromBlocks():

        mdm = MarvelousDesignerModule()
        ## Enable drapping
        mdm.SimulationOn(1)
            
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Dropped.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_ButtonDown--Sleeves_Raglan_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_ButtonDown--Sleeves_Raglan_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_Traditional--Sleeves_Raglan_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_Traditional--Sleeves_Raglan_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_ButtonDown--Sleeves_Raglan_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_ButtonDown--Sleeves_Raglan_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_Traditional--Sleeves_Raglan_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_Traditional--Sleeves_Raglan_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_ButtonDown--Sleeves_Raglan_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_ButtonDown--Sleeves_Raglan_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_Traditional--Sleeves_Raglan_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Raglan.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Raglan.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar_Raglan.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Raglan.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_Traditional--Sleeves_Raglan_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Dropped.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.Regular.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideVent.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.ButtonDown.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Dropped.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Long.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
                           
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Polo.Set-In.zmdr", [r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Body_Set-In.SideZip.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Collar.Traditional.zblc", r"/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos\Sleeves_Set-In.Short.zblc"])
                    
        # Create the Garment file
        mdm.ExportZPac(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
                           

    @staticmethod
    def createProjectsAndImagesFromGarments(object):
        # Garments to Images & Projects

        # clear console window
        object.clear_console() 
        #initialize object module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")

        #Set simulation property settings
        #Set Simulation property options(simulation quality) of integer type
        # qulity = 0 Complete
        # qulity = 1 Normal
        # qulity = 2 Custom
        object.set_simulation_quality(1)

        # Attempting to take the later frames of the simulation
        object.set_simulation_options(0, 0, 10000)

        # Load the avatar
        object.set_avatar_file_path(r"C:\Users\Public\Documents\CLO\Assets\Avatar\Avatar\Female_V2\Avatar (Modular)\Modular_FV2_Feifei.avt")
        object.set_avatar_file_path(r"C:\Users\Public\Documents\CLO\Assets\Avatar\Avatar\Female_V1\FV1_Emma.avt")
        object.set_avatar_file_path(r"C:\Users\Public\Documents\CLO\Assets\Avatar\Avatar\Female_V2\FV2_Feifei.avt")


        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Dropped____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_ButtonDown--Sleeves_Raglan_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_ButtonDown--Sleeves_Raglan_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_Traditional--Sleeves_Raglan_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideVent--Collar_Raglan_Traditional--Sleeves_Raglan_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_ButtonDown--Sleeves_Raglan_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_ButtonDown--Sleeves_Raglan_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_Traditional--Sleeves_Raglan_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_SideZip--Collar_Raglan_Traditional--Sleeves_Raglan_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_ButtonDown--Sleeves_Raglan_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_ButtonDown--Sleeves_Raglan_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_Traditional--Sleeves_Raglan_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Raglan____Body_Raglan_Regular--Collar_Raglan_Traditional--Sleeves_Raglan_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Dropped_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_Regular--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideVent--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_ButtonDown--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Dropped_Short.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Long.zpac')
        object.sync_file_lists("animation")
                        
        #next multi process
        object.set_garment_file_path(r'clobot/output\Polo_Set-In____Body_Set-In_SideZip--Collar_Traditional--Sleeves_Set-In_Short.zpac')
        object.sync_file_lists("animation")
                        

        object.set_save_folder_path(r'clobot/output', "obj")

        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(True)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()
    