import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
<<<<<<< HEAD
  }

=======
    this.loginform = new FormGroup({
      'email' : new FormControl(null, [Validators.required, Validators.email]),
      'password':new FormControl(null, Validators.required)
    }); 
 
  }
  get email() {
    return this.loginform.get('email');
  }
  get password() {
    return this.loginform.get('password');
  }
    loginform = this.fb.group({
    email : ['',Validators.required, Validators.email],
    password : ['',Validators.required]
    })
  logins(){ 
    console.log(this.loginform.value)
    this.lService.logins(this.loginform.value).subscribe(response =>{
      alert("login successful");
     console.log(response)
     this.router.navigate(['masterpage']) 
    },err=>{
      alert("Invalid Username Password")
    })
  }
  
>>>>>>> 6fc0f60b6683a1c5a200dc2360fb80bb5c99a16c
}
