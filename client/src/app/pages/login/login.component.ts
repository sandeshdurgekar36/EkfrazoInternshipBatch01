import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
    login!: FormGroup;
 
  ngOnInit(): void {
    this.login! = new FormGroup({
     'username':new FormControl(null, Validators.required),
     'password':new FormControl(null, Validators.required)
  });
  }
  get username() {
    return this.login!.get('username');
  }
  get password() {
    return this.login!.get('password');
  }
}
