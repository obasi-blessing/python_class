class Smartphone:
    def __init__(self, brand, model, storage, battery):
        
        self.brand = brand
        self.model = model
        self.storage = storage  
        self.battery = battery  
        self.is_on = False
        self.apps = []  

    
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.brand} {self.model} is now ON."
        return f"{self.brand} {self.model} is already ON."

    def power_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.brand} {self.model} is now OFF."
        return f"{self.brand} {self.model} is already OFF."

    def install_app(self, app_name):
        if self.is_on:
            self.apps.append(app_name)
            return f" {app_name} installed on {self.model}."
        return f" Cannot install apps while {self.model} is OFF."

    def list_apps(self):
        return f"Installed apps on {self.model}: {', '.join(self.apps) if self.apps else 'No apps yet.'}"

    def take_photo(self):
        if self.is_on:
            return f"📸 {self.brand} {self.model} takes a photo!"
        return f" Cannot take photo. {self.model} is OFF."

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}mAh)"
