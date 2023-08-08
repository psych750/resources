from psychopy import visual, gui, prefs
import webbrowser

runtime_variables = {'Name':'Enter your name', 'Email':'Enter your full @wisc.edu email'}
dlg = gui.DlgFromDict(runtime_variables,order=['Name','Email'])

user_prefs = str(prefs.paths)+str(prefs.userPrefsCfg)

survey_url = f"https://docs.google.com/forms/d/e/1FAIpQLSeGwIzV-2_0-iQKKSBq8vadYH7mMrWtq9hA35zWqkOYRQ_Wxw/viewform?usp=pp_url&entry.221237748={runtime_variables['Name']}&entry.1474916019={runtime_variables['Email']}&entry.812117808={user_prefs}"

webbrowser.open_new(survey_url)