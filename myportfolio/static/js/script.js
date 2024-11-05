function openApp(app) {
    // Hide all app windows
    const apps = document.querySelectorAll('.app-window');
    apps.forEach((window) => {
      window.style.display = 'none';
    });
  
    // Redirect to GitHub
    if (app === 'github') {
      window.open('https://github.com/najouaelfethi', '_blank');
      return;
    }
      // Redirect to Resume
    if (app === 'resume') {
        window.open("{% static 'docs/CV_NAJOUA_ELFETHI.pdf' %}", '_blank'); 
        return;

    // Show the selected app window
    const selectedApp = document.getElementById(app);
    if (selectedApp) {
      selectedApp.style.display = 'block';
    }
  }
  
  function closeApp(app) {
    const selectedApp = document.getElementById(app);
    if (selectedApp) {
      selectedApp.style.display = 'none';
    }
  }


}