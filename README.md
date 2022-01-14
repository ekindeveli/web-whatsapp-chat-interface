# web-whatsapp-chat-interface
 A chatting interface that uses Whatsapp Web to send and retrieve messages

### THIS IS THE PRODUCT AS DELIVERED, WITH THE EXCEPTION OF COMMENTS AND VARIABLES ADDED OR TRANSLATED TO ENGLISH ###
First Start Requirements, needs to be run only once:

1- Copy the program files and install dependencies using "requirements.txt"

2- Run the FirefoxSettings.py file. This file modifies "profiles.ini" to add the profile that will be used.
This program needs to be run only once. If your Firefox installation or profiles are located in a non-default path,
please edit Line 27 of the FirefoxSettings.py file (to correctly point to Firefox profile settings file).

3- Manually start firefox, select "whatsweb" profile. Connect to "web.whatsapp.com" and login using the QR code.

*** Without running these 3 steps before first use, the program will not run properly. ***

As mentioned, these steps have to be completed only once. Only exception is logging into Web Whatsapp via QR code,
which has to be repeated when logged out of Web Whatsapp e.g. via browser history erasure, modem reset etc.

Simply run "WhatsEnteg.py" to run the program and manage from Command Line Interface,
or delete code indicated below and call the functions from other files. Deleting code is not necessary if only calling
functions from other files and not the whole WhatsEnteg.py file.

====================================================================================================================

- This messaging interface is integrated into a local government desktop application and is hidden behind a GUI.
The government workers can communicate between each other, as well as with the general public although
in a more limited manner.

- User may send and view messages using either contact name or phone number. Entering phone number might result
in erroneously sending messages to a group that the phone number's holder is in. I was told that this wont be a problem
since there will be no groups, and even if there were they would include only government employees (i.e saved contacts).

- New messages don't need to be immediately synchronized, the GUI will have a refresh button that will
call the message retriever function. "You have X unread messages, refresh to view" functionality may be implemented
in the future.

- Retrieving recent messages satisfies desired functionality, no need to retrieve entire chat history
i.e. dont have to deal with scrolling and retrieving new objects on the Selenium client.

- The ability to "save as contact" or "start new chat" not wanted as those will be provided
separately within the GUI.

- To turn on the "headless" option, i.e. make invisible the Firefox Browser that runs Whatsapp Web,
 set the "options.headless" variable to "True" inside the "initializer()" function of the WhatsEnteg.py file.