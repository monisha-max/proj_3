from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

symptoms_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
                 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
                 'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings',
                 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
                 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache',
                 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',
                 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
                 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
                 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
                 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate',
                 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain',
                 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels',
                 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremities', 'excessive_hunger',
                 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
                 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements',
                 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
                 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
                 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium',
                 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes',
                 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum',
                 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
                 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
                 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
                 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
                 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
                 'red_sore_around_nose', 'yellow_crust_ooze']

diseases = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
            'Peptic ulcer disease', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
            'Migraine', 'Cervical spondylosis',
            'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
            'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
            'Common Cold', 'Pneumonia', 'Dimorphic hemorrhoids(piles)', 'Heart attack', 'Varicose veins',
            'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthritis', 'Arthritis',
            '(vertigo) Paroymsal Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']

symptom_flags = []
for _ in range(len(symptoms_list)):
    symptom_flags.append(0)

# TESTING DATA
testing_data = pd.read_csv("Testing.csv")
testing_data.replace({'prognosis': {disease[i]: i for i in range(len(diseases))}}, inplace=True)

X_test = testing_data[symptoms_list]
y_test = testing_data[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
training_data = pd.read_csv("Training.csv")
training_data.replace({'prognosis': {disease[i]: i for i in range(len(diseases))}}, inplace=True)

X_train = training_data[symptoms_list]
y_train = training_data[["prognosis"]]
np.ravel(y_train)


def message():
    if (Symptom1.get() == "None" and Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None"
            and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else:
        NaiveBayes()


def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb = gnb.fit(X_train, np.ravel(y_train))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(symptoms_list)):
        for z in psymptoms:
            if z == symptoms_list[k]:
                symptom_flags[k] = 1

    input_test = [symptom_flags]
    predict = gnb.predict(input_test)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(diseases)):
        if diseases[predicted] == diseases[a]:
            h = 'yes'
            break

    if h == 'yes':
        t3.delete("1.0", END)
        t3.insert(END, diseases[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")


root = Tk()
root.title(" Disease Prediction From Symptoms")
root.configure()

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10, sticky=W)

S1Lb = Label(root, text="Symptom 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

lr = Button(root, text="Predict", height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1, pady=20)

OPTIONS = sorted(symptoms_list)

S1En = OptionMenu(root, Symptom1, *OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Symptom2, *OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Symptom3, *OPTIONS)
S3En.grid(row=9, column=2)

S4En = OptionMenu(root, Symptom4, *OPTIONS)
S4En.grid(row=10, column=2)

S5En = OptionMenu(root, Symptom5, *OPTIONS)
S5En.grid(row=11, column=2)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10, sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10, sticky=W)

t3 = Text(root, height=2, width=30)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1, padx=10)

root.mainloop()
