import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('google.auth', scope)

gc = gspread.authorize(credentials)

#sh = gc.create('users')
#sh.share('illariojane@gmail.com', perm_type='user', role='writer')

def find_permission(user):

	wks = gc.open("users").sheet1
	all_rows = wks.get_all_values()
	user_emails = [item[0] for item in all_rows]
	user_permissions = [item[1] for item in all_rows]
	
	try:
		user_index = user_emails.index(user)
	except ValueError:
		user_index = -1

	if user_index >= 0:
		#print(user_index, user_permissions[user_index])
		return user_permissions[user_index]

	#wks.update_acell('B2', "it's down there somewhere, let me take another look.")

	# Fetch a cell range
	#cell_list = wks.range('A1:B7')

def input_data(form, permission):
	print(repr(form))
	print(form)
	wks = gc.open("Catalist").sheet1
	index = len(wks.get_all_values()) + 1
	wks.update_cell(index, 1, form.date.data.strftime("%B %d, %Y"))
	wks.update_cell(index, 2, form.name.data)
	wks.update_cell(index, 3, form.date_of_birth.data.strftime("%B %d, %Y"))
	wks.update_cell(index, 4, form.age.data)
	wks.update_cell(index, 5, form.sex.data)
	wks.update_cell(index, 6, form.description.data)
	wks.update_cell(index, 7, form.sn.data)
	wks.update_cell(index, 8, form.shelter_name.data)
	wks.update_cell(index, 9, form.shelter_id.data)
	#wks.update_cell(index, 10, form.photo.data)
	wks.update_cell(index, 11, form.fiv_tested.data)
	wks.update_cell(index, 12, form.flv_tested.data)
	wks.update_cell(index, 13, form.fvrcp_vaccination_date.data.strftime("%B %d, %Y"))
	wks.update_cell(index, 14, form.rabies_vaccination_date.data.strftime("%B %d, %Y"))
	wks.update_cell(index, 15, form.medical_notes.data)
	#wks.update_cell(index, 16, form.medical_documents.data)
	wks.update_cell(index, 17, form.behaviour_notes.data)
	wks.update_cell(index, 18, form.urgent.data)
	wks.update_cell(index, 19, form.petpoint_id.data)
	wks.update_cell(index, 20, form.outcome.data)
	if form.intake_date.data is not None:
		wks.update_cell(index, 21,form.intake_date.data.strftime("%B %d, %Y"))
	if form.foster_placement_date.data is not None:
		wks.update_cell(index, 22,form.foster_placement_date.data.strftime("%B %d, %Y"))
	wks.update_cell(index, 23,form.location.data)
	if permission is 'foster':
		wks.update_cell(index, 24, 'foster')
	elif permission is 'shelter':
		wks.update_cell(index, 24, 'shelter')
	elif permission is 'intake':
		wks.update_cell(index, 24, 'intake')
