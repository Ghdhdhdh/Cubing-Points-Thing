function submit() {
    
    var solvetime = document.getElementById('time').value
    var team = document.getElementById('team').value

    document.location = '/submit?time=' + solvetime + '&team=' + team
}