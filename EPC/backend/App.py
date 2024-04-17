from flask import Flask, request, jsonify
from flask_cors import CORS
from process_images import extract_text_from_image
from check_answer import check_answer

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/upload', methods=['POST'])
def upload_images_route():
    try:
        # Get the 'type' value from formData
        image_type = request.form.get('type')

        original_image = request.files.get('originalImage')
        student_image = request.files.get('studentImage')

        if not (original_image and student_image):
            response_data = {'message': 'Both originalImage and studentImage are required.'}
            return jsonify(response_data), 400

        original_text = extract_text_from_image(original_image)
        student_text = extract_text_from_image(student_image)

        # print(original_text)
        # print(student_text)


        result,total=check_answer(image_type, original_text,student_text)


        # You can now use 'original_text' and 'student_text' for further processing
        # For example, return them in the response
        print("you obtained ",result," out of ",total)
        response_data = {
            'message': 'Images uploaded and processed successfully',
            'total': total,
            'result': result
        }
        return jsonify(response_data), 200

    except Exception as e:
        response_data = {'message': f'Upload and processing failed: {str(e)}'}
        return jsonify(response_data), 500

if __name__ == '__main__':
    app.run()
