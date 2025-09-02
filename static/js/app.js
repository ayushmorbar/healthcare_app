document.addEventListener('DOMContentLoaded', function() {
    // Password confirmation validation
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');
    
    if (password1 && password2) {
        function validatePasswordMatch() {
            if (password1.value && password2.value) {
                if (password1.value === password2.value) {
                    password2.setCustomValidity('');
                    password2.classList.remove('is-invalid');
                    password2.classList.add('is-valid');
                } else {
                    password2.setCustomValidity('Passwords do not match');
                    password2.classList.remove('is-valid');
                    password2.classList.add('is-invalid');
                }
            }
        }
        
        password1.addEventListener('input', validatePasswordMatch);
        password2.addEventListener('input', validatePasswordMatch);
    }
    
    // Pincode validation
    const pincodeField = document.getElementById('id_pincode');
    if (pincodeField) {
        pincodeField.addEventListener('input', function() {
            const value = this.value;
            if (value && !/^\d{6}$/.test(value)) {
                this.setCustomValidity('Pincode must be exactly 6 digits');
                this.classList.add('is-invalid');
            } else {
                this.setCustomValidity('');
                this.classList.remove('is-invalid');
                if (value) this.classList.add('is-valid');
            }
        });
    }
    
    // Auto-dismiss alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            if (typeof bootstrap !== 'undefined') {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    });
    
    // Profile picture preview
    const profilePictureInput = document.getElementById('id_profile_picture');
    if (profilePictureInput) {
        profilePictureInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            const existingPreview = document.getElementById('profile-preview');
            
            if (existingPreview) {
                existingPreview.remove();
            }
            
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const preview = document.createElement('img');
                    preview.id = 'profile-preview';
                    preview.className = 'mt-2 img-thumbnail';
                    preview.style.maxWidth = '150px';
                    preview.style.maxHeight = '150px';
                    preview.src = e.target.result;
                    profilePictureInput.parentNode.appendChild(preview);
                };
                reader.readAsDataURL(file);
            }
        });
    }
});
