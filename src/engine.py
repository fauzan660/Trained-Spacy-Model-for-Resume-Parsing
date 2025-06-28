
from ML_Pipeline import predict_model
from ML_Pipeline import utils



print("Done. Converted into spacy format")

print(
    "Checking if previously built spacy model exists. If not, we will train a new one"
)

model = utils.check_existing_model("nlp_model")

print(predict_model.predict("../junior_frontend_resume.pdf"))

