This repo contains automated script to join all clients fb_ads metrics for test_case usage. 
The files need to be downloaded manually using [this template](https://adsmanager.facebook.com/adsmanager/reporting/view?act=267439853604540&business_id=822980251078828&event_source=CLICK_CUSTOMIZE_REPORT&global_scope_id=822980251078828&selected_report_id=6637578216344&source=share&breakdown_regrouping=1&nav_source=no_referrer) for all of the clients first.
Don't forget to change the time period first before download and make sure to use the `.xlsx` format and turn off summary.

Before running the script, here are simple step by step that needed to be done:
- Create a virtual environment with the libary from `requirements.txt`
- Make a folder named `data`, then move all of the downloaded data here

After we have all of the client's data inside `data` folder, below are step by step to run the script.
- Please check your folder location, make sure to set them to this repo folder
- Activate your virtual environment
  ```cmd
  conda activate your_venv_name
  ```
- Run the script
  ```cmd
  python concat_data.py
  ```

The merged data then will be written to file named `concat_data.xlsx`
