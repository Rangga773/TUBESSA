from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

def brute_force_password(charset, max_length, verify_function):
    def generate_combinations(current_combination, length):
        if length == 0:
            if verify_function(current_combination):
                return current_combination
            return None
        for char in charset:
            result = generate_combinations(current_combination + char, length - 1)
            if result:
                return result
        return None

    for length in range(1, max_length + 1):
        result = generate_combinations("", length)
        if result:
            return result
    return None

def divide_and_conquer_password(charset, max_length, verify_function):
    def helper(prefix, length):
        if length == 0:
            if verify_function(prefix):
                return prefix
            return None
        for char in charset:
            result = helper(prefix + char, length - 1)
            if result:
                return result
        return None

    for length in range(1, max_length + 1):
        result = helper("", length)
        if result:
            return result
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crack_password', methods=['POST'])
def crack_password():
    data = request.json
    algorithm = data['algorithm']
    charset = data['charset']
    max_length = int(data['max_length'])
    correct_password = data['correct_password']

    def verify_function(candidate):
        return candidate == correct_password

    start_time = time.perf_counter()
    if algorithm == 'bruteforce':
        found_password = brute_force_password(charset, max_length, verify_function)
    elif algorithm == 'dnc':
        found_password = divide_and_conquer_password(charset, max_length, verify_function)
    end_time = time.perf_counter()

    duration = end_time - start_time
    return jsonify({
        'algorithm': algorithm,
        'found_password': found_password,
        'duration': duration,
        })

if __name__ == '__main__':
    app.run(debug=True)
