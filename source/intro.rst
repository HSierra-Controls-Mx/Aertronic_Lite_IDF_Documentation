AERtronic Lite V2.0
===================
 
.. warning::
   This project is under continuous development and still in early beta phase.
 
The **AERtronic Lite** aims to be a more affordable solution compared to the current AERtronic Basic hardware and software. The main objective of the project is to be cheaper than the existing solution that uses the same module for three AERtronic variants: Basic, Advanced, and Premium.
 
In this project, we will develop a new user interface by taking advantage of the new Nextion Intelligent HMI 7'' display, which offers more resources to work with. This will result in a more robust and appealing design. Regarding the MCU, we will also replace the ESP32 board with the Wireless-tag WT32-ETH01, which is an embedded serial-to-Ethernet module based on the ESP32 series.
 
The **AERtronic Lite** will be best suited for machines that require a display to show the current values of pressure and temperature, machines that only have an analog indicator or for equipment that requires a track of maintenance activities, event logs and communication to other devices such as DO probes, SCADAs, PLCs, etc.
 
The solution consists of a 7'' display, the same size of the original AERtronic 2.0. An electronic board will be the responsible to handle the input of the pressure and temperature sensor. This board will include three digital outputs for the client to use. As mentioned before we will use the Wireless-tag WT32-ETH01 MCU to control the whole system, PlatformIO will be the main IDE to program and update this microprocessor.
 
The user interface will be developed from the scratch. The design follows the Google Material 3 design guidelines to maintain a good user experience throughout the whole system.
 
Legacy projects
---------------
 
If you are looking for previous version of the **AERtronic Lite** project please check the below links:
 
.. note::
    For the original repository, please refer to this link: `AERtronic Lite Deprecated <https://github.com/ErnestoAerzen/AERtronic>`_
 
.. note::
    For the latest repository release, please refer to this link: `AERtronic Lite PlatformIO Update <https://github.com/ErnestoAerzen/AERtronic-Lite>`_
 
Technology
----------
 
We use a variaty of languages and software technologies to develop **AERtronic Lite** such as:
 
* The entire MCU system is programmed using C++, the display uses a combination of ASCII text and hexadecimal commands to add functionality to the user interface.
* PlatformIO Visual Studio Code extension.
* Nextion Editor.
* Electronic board developed from the scratch using Proteus software.
* Adobe XD and Figma platform to prototype the user interface.
* Wireless-tag WT32-ETH01 MCU board.
* Serial comunication between the MCU and the Nextion display to increase system functionality.
 
.. note::
    Every Nextion page is a combination of ASCII instructions and Nextion built-in objects.
 
External links
--------------
 
These are the links to the main technologies used in the project:
 
* `Download Nextion Editor <https://nextion.tech/nextion-editor/>`_
* `Reference to ASCII table <https://ascii-tables.com/>`_
* `ESP32 time library <https://github.com/fbiego/ESP32Time>`_
* `Reference to Nextion instruction set <https://nextion.tech/instruction-set>`_
 
.. warning::
    For future versions of AERtronic Lite the use of external libraries will be removed. Use the releated features with discretion.
 
Troubleshooting
---------------
 
.. important::
    Only qualified personnel can operate with the electronic board and the cable connections in order to prevent any accident.
 
* Ensure that all the connections are made correctly and securely.
* Check that you have selected the correct board and port in Visual Studio Code editor.
* Verify that the libraries are properly installed and up to date.
* If encountering any issues with sensor readings, double-check the sensor connections and consult their respective datasheets.
 
Design
------
 
The new user interface of the **AERtronic Lite** is going to have a fresh new style based on the guidelines of material design 3 by Google focusing in keeping things as clear as possible.
We will follow the AERZEN coorporate guidelines including typography, color pallet, images and videos to align with the company's requirements.
 
.. important::
    `Guideline specifications of AERZEN's logo design <https://www2.aerzen.com/amp-ci-portal/corporate-design-specifications/brand-symbollogotype.html>`_
 
Serial Communication
--------------------
 
We will utilize hexadecimal codes to transmit commands over serial communication between the Nextion display and the MCU. All codes adhere to the Nextion Instruction Set documentation. For further details, please refer to the `Nextion Instruction Set <https://nextion.tech/instruction-set/#s7>`_.
 
+-----------+-----------------------+--------------------------------------------------------------------------------+
| Hex value | Code name             | Description                                                                    |
+===========+=======================+================================================================================+
| 0x00      | Nextion startup       | Returned when the display has started or reset.                                |
+-----------+-----------------------+--------------------------------------------------------------------------------+
| 0x24      | Serial buffer overflow| Returned when a serial buffer overflow occurs. Buffer will continue to receive |
|           |                       | the current instruction, all previous instructions are lost.                   |
+-----------+-----------------------+--------------------------------------------------------------------------------+
| 0x66      | Current page number   | Returned when the sendme command is used.                                      |
+-----------+-----------------------+--------------------------------------------------------------------------------+
| 0x70      | String Data Enclosed  | Returned when using get command for a string. Used in the project to receive   |
|           |                       | the defined time and date by the user. See get command in the Nextion          |
|           |                       | Instruction Set documentation.                                                 |
+-----------+-----------------------+--------------------------------------------------------------------------------+
 
Contributing
------------
 
This is a private project, pull requests will be only accepted by the designated developers and approved by the main project developer.
Commits will only be added to the main branch when they have passed all the tests and being bug-free.
 
Developed with love in Mexico ❤️🇲🇽