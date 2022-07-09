import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { LoginService } from 'src/app/services/login.service';  '../services/login.service';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router'; 


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  
      
    constructor(private lService: LoginService,private fb:FormBuilder,private router:Router) { }
 
  ngOnInit(): void {
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
  
}
