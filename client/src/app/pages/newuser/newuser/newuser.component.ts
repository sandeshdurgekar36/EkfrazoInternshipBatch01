import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';

@Component({
  selector: 'app-newuser',
  templateUrl: './newuser.component.html',
  styleUrls: ['./newuser.component.css']
})
export class NewuserComponent implements OnInit {
  nuser!: FormGroup;
  

  constructor() { }

  ngOnInit(): void { 
    this.nuser! = new FormGroup({
      'username':new FormControl(null, Validators.required),
      'password':new FormControl(null, Validators.required),
      'email' : new FormControl(null, [Validators.required, Validators.email]),    
      'first_name':new FormControl(null, Validators.required),
      'last_name':new FormControl(null, Validators.required),
      
   });
  }
  get username() {
    return this.nuser!.get('username');
  }
  get password() {
    return this.nuser!.get('password');
  }
  get email() {
    return this.nuser!.get('email');
  }
  get last_name() {
    return this.nuser!.get('last_name');
  }
  get first_name() {
    return this.nuser!.get('first_name');
  }
  

}
