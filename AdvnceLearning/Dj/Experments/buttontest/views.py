from django.shortcuts import render

def increment(request):
    # Retrieve the counter and step values from the session
    counter = request.session.get('counter', 0)
    step = request.session.get('step', 0)

    # Check if the request is a POST request
    if request.method == 'POST':
        if step >= 3:
            step = 0

        # Increment the counter
        counter += 1
        step += 1

    # Save the counter and step values back to the session
    request.session['counter'] = counter
    request.session['step'] = step

    # Pass the updated counter value and step to the template
    return render(request, 'buttontest.html', context={'value': counter, 'step': step})
