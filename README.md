<h4 align="center">
<img src="https://github.com/epessina/LandslidesSurvey/blob/master/App/screens/logo.png" width="144" alt="Logo">
</h4>

# LandslidesSurvey QGIS Plugin

LandslidesSurvey QGIS Plugin is a plugin for QGIS 3 developed to easily retrieve all the data inserted through the
smartphone application [LandslidesSurvey](https://github.com/epessina/LandslidesSurvey). 

The plugin call the open RESTFul API of LandslidesSurvey and queries the database for all the landslides inserted.
The data can be filtered by the user using a vector layer and can be downloaded both in JSON format and as a Shapefile.


## Installation

The plugin works with any version of QGIS 3 and does not require any additional dependency.

1. Download [LandslidesSurvey-x.x.x.zip](https://github.com/epessina/LandslidesSurvey-QGIS-Plugin/releases)
2. Open QGIS.
3. Navigate to `Plugins > Manage and Install Plugins...`.
4. Open the tab `Install from ZIP`.
5. Select the previously downloaded zip file and click on `Install Plugin`.
6. Done!

If the plugin does not appears automatically on the toolbar, navigate to `Plugins > Manage and Install Plugins... > 
Installed` and make sure that the checkbox beside LandslidesSurvey is checked.


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/#) © [Edoardo Pessina](edoardo2.pessina@mail.polimi.it)