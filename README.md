# WhatsApp_Message_Sender
This project automates the process of sending a message to multiple phone numbers on WhatsApp using Selenium and Python. It extracts phone numbers from a WhatsApp group, and saves them to an Excel file. Then, it formats the phone numbers and sends a custom message to each number using the WhatsApp Web interface.


Installation:
1. Install Python (version 3.7 or above) from the official website.
2. Install the appropriate Chrome WebDriver for your version of Chrome from [chromedriver](https://chromedriver.chromium.org/downloads) and save it in the same project file . 
3. Install the required Python packages by running the following command in your terminal:

   pip install re
   
   pip install openpyxl
   
   pip install selenium
   
   pip install pyautogui
   


Usage:
1. Make sure you have Google Chrome installed on your system.
2. Make sure you have Whatsapp Desktop on your system and logged in with your account.
3. Clone or download this project from GitHub.
4. Open the project directory in your terminal or code editor.
5. Update the `group_name` and `input_message` variables in the script with the name of your target WhatsApp group and the message you want sent to each number of group.
6. Run the script by executing the following command:
   whatsapp_message_sender.py
7. Follow the instructions to scan the QR code and log in to WhatsApp Web.
8. The script will automatically find the target group, extract phone numbers, saves them to an Excel file and send the message.
9. Follow this steps at frist message you have 20 sec. to do that , Don't miss the opportunity! :"
     ![steps](https://github.com/MahmoudEmadSlman/WhatsApp_Message_Sender/assets/84009205/25ca9d81-db34-4503-9ba3-09c262e61bfc)

Note: Please use this script responsibly and respect the privacy of others. Make sure you have the necessary permissions before sending messages to anyone.

Contributing:
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request on the GitHub repository.

Credits:
- Author: Mahmoud Emad Slman
- Email: eng.mahmoud.slman@gmail.com
