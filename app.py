from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Total parking slots
TOTAL_SLOTS = 10

# None = Free, otherwise stores vehicle number
slots = [None] * TOTAL_SLOTS


# Home page
@app.route('/')
def index():
    return render_template('index.html', slots=slots)


# Book slot (GET = show form, POST = submit vehicle)
@app.route('/book/<int:slot_id>', methods=['GET', 'POST'])
def book(slot_id):
    if 0 <= slot_id < TOTAL_SLOTS:

        # When user submits vehicle number
        if request.method == 'POST':
            vehicle = request.form.get('vehicle')

            if vehicle:
                slots[slot_id] = vehicle

            return redirect(url_for('index'))

        # When user clicks "Book"
        return render_template('book.html', slot_id=slot_id)

    return redirect(url_for('index'))


# Release slot
@app.route('/release/<int:slot_id>')
def release(slot_id):
    if 0 <= slot_id < TOTAL_SLOTS:
        slots[slot_id] = None

    return redirect(url_for('index'))


# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)