let siteName = window.prompt("enter your fav site (Like google.com):");
if (window.confirm(`Do you want to open ${siteName}?`)){
    const windowFeatures = "left=100, top=100, width=320, height=320";
    const siteLink = `https://www.${siteName}`;
    const handle = window.open(
        siteLink,
        `${siteName.substring(0,siteName.indexOf("."))}Window`,
        windowFeatures,
    );
    if(handle){
        return "window is opened";
    } else{
        return "unable to open window";
    }
}