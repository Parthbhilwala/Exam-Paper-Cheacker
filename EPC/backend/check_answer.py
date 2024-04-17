from paracheck import theoretical

def check_answer(image_type,original, student):

    if image_type == "mcq" or image_type == "tf" or image_type == "word":
    # Split both strings into words by spaces
        original_words = original.split()
        student_words = student.split()

        # Ensure both lists of words have the same length
        if len(original_words) != len(student_words):
            return "Strings have different word counts"

        # Initialize a variable to keep track of the count of non-matching words
        non_matching_count = 0

        # Iterate through the words in both lists and compare them
        for i in range(len(original_words)):
            if original_words[i] != student_words[i]:
                non_matching_count += 1

        return len(original_words) - non_matching_count, len(original_words)
    elif image_type=="para":
        return theoretical(student,original)


