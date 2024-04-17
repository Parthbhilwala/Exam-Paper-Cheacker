import transformers
import torch
from scipy.spatial.distance import cosine


tokenizer = transformers.BertTokenizer.from_pretrained('bert-large-uncased')
model = transformers.BertModel.from_pretrained('bert-large-uncased')

exam_paper = "(a) Transition elements are elements with partially filled d orbitals (also known as transition metals). Transition elements are defined by IUPAC as elements with a partially filled d subshell or elements capable of forming stable cations with an incompletely filled d orbital. The transition element's electronic configuration is (n-1)d5 ns1 or (n-1)d10 ns1. Since their valence electrons are in two different sets of orbitals, (n-1)d and ns, these elements have variable oxidation states. The energy difference between these orbitals is so small that both energy levels can be used to form bonds. As a result, transition elements have variable oxidation states. 1. Mn(Z-25) has the highest number of unpaired electrons in the d-subshell, and it shows a high oxidation state(+7). 2. Scandium (Sc) only exhibits a +3 oxidation state in these series.(b) The steady decrease in atomic and ionic radii (with the same charge) with increasing atomic number as we move from lanthanum to lutetium is referred to as lanthanoid contraction. Mischmetal is an important lanthanoid metal alloy that contains 95 lanthanide metal and 5 Fe, as well as traces of S, C, Ca, and Al. It is used to make bullets, shells, and lighter flint in Mg-based alloys."
answer_key = "(a) Transition elements show variable oxidation states due to the presence of incompletely filled d orbitals in their electron configurations. The d orbitals can accommodate different numbers of electrons, allowing transition metals to lose different numbers of electrons and thus exhibit multiple oxidation states.The first series of transition metals from Scandium (Sc, Z = 21) to Zinc (Zn, Z = 30) includes elements like Scandium, Titanium, Vanadium, Chromium, Manganese, Iron, Cobalt, Nickel, and Copper. Among these, Chromium (Cr) and Manganese (Mn) exhibit the maximum number of oxidation states. Chromium can have oxidation states ranging from -2 to +6, while Manganese can have oxidation states from -3 to +7.The element that shows only a +3 oxidation state in this series is Scandium (Sc). (b) Lanthanide contraction refers to the decrease in the size of the 4f orbitals of lanthanide elements as you move from left to right across the lanthanide series. This contraction occurs because the additional electrons are added to the same 4f subshell, leading to poor shielding of the increasing nuclear charge. An important alloy that contains some of the lanthanoid (lanthanide) metals is 'Mischmetal.' Mischmetal is a rare earth element mixture that primarily consists of cerium and lanthanum along with small amounts of other lanthanides. It is often used in the production of flints for lighters and various other metallurgical applications due to its ability to produce sparks when struck against a rough surface."
exam_paper_tokens = tokenizer(exam_paper, return_tensors='pt')
answer_key_tokens = tokenizer(answer_key, return_tensors='pt')

# Create a dictionary with the input data
input_data_exam = {
    "input_ids": exam_paper_tokens["input_ids"],
    "attention_mask": exam_paper_tokens["attention_mask"]
}

input_data_answer_key = {
    "input_ids": answer_key_tokens["input_ids"],
    "attention_mask": answer_key_tokens["attention_mask"]
}

# Pass the input data dictionaries to the BERT model
exam_paper_embeddings = model(**input_data_exam)[0]
answer_key_embeddings = model(**input_data_answer_key)[0]

# Calculate the cosine similarity using scipy
similarity_score = 1 - cosine(
    exam_paper_embeddings[0].mean(0).detach().numpy(),
    answer_key_embeddings[0].mean(0).detach().numpy()
)

print(similarity_score)

