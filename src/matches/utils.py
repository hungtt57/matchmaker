from django.contrib.auth import get_user_model
from decimal import Decimal
from questions.models import UserAnswer

# User = get_user_model()

# users = User.objects.all() #[user1 ,user2]
# all_user_answers = UserAnswer.ojbjects.all().order_by("user_id")



# def get_match(user_a,user_b):
# 	user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
# 	user_b_answers = UserAnswer.objects.filter(user=user_b)[0]

# 	if user_a_answers.question.id == user_b_answers.question.id:
# 		user_a_answer = user_a_answers.my_answer
# 		user_a_pref = user_a_answers.their_answer
# 		user_b_answer= user_b_answers.my_answer
# 		user_b_pref = user_b_answers.their_answer

# 		user_a_total_awarded = 0
# 		user_b_total_awarded = 0
# 		if user_a_answer = user_b_pref:
# 			user_b_total_awarded += user_b_answers.their_points
# 			print "user a fits with user b's preference"
# 		if user_a_pref == user_b_answer:
# 			user_a_total_awarded += user_a_answers.their_points
# 			print "user b fit user a pref"

# 		if user_a_answer == user_b_pref &&user_a_pref == user_b_answer:
# 			print "this is an idel answer for both"

def get_points(user_a,user_b):
	a_answers = UserAnswer.objects.filter(user=user_a)
	b_answers = UserAnswer.objects.filter(user=user_b)
	a_total_awarded = 0
	a_points_possible = 0
	num_question = 0
	for a in a_answers:
		for b in b_answers:
			if a.question.id == b.question.id:
				num_question +=1
				a_pref = a.their_answer
				b_answer = b.my_answer
				if a_pref == b_answer:
					'''
					awards points for correct answer
					'''
					a_total_awarded += a.their_points
				''' assiging total points '''

				a_points_possible += a.their_points

			print "%s has awarded %s points of %s to %s" %(user_a,a_total_awarded,a_points_possible,user_b)
	percent = a_total_awarded / Decimal(a_points_possible)
	print percent,num_question
	if percent == 0:
		percent = 0.000001
	return percent,num_question


def get_match(user_a,user_b):
	a = get_points(user_a,user_b)
	b = get_points(user_b,user_a)

	#a[0] = decimal match value
	# b[1]/a[1] = number pf questions anwered
	number_of_questions = b[1]
	match_decimal = (Decimal(a[0]) * Decimal(b[0])) ** (1/Decimal(number_of_questions))
	return match_decimal,number_of_questions
