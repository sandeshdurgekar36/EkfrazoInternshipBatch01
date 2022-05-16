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
    'phone' : new FormControl(
      null,
      [
        Validators.required,
        Validators.pattern('^\\s*(?:\\+?(\\d{1,3}))?[-. (]*(\\d{3})[-. )]*(\\d{3})[-. ]*(\\d{4})(?: *x(\\d+))?\\s*$')
      ]),
      'funame':new FormControl(null, Validators.required),
      'dob':new FormControl(null, Validators.required),
      'city':new FormControl(null, Validators.required),
      'state':new FormControl(null, Validators.required),
      'address':new FormControl(null, Validators.required),
      'pincode':new FormControl(null, Validators.required),
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
  get phone() {
    return this.nuser!.get('phone');
  }
  get funame() {
    return this.nuser!.get('funame');
  }
  get dob() {
    return this.nuser!.get('dob');
  }
  get city() {
    return this.nuser!.get('city');
  }
  get state() {
    return this.nuser!.get('state');
  }
  get address() {
    return this.nuser!.get('address');
  }
  get pincode() {
    return this.nuser!.get('pincode');
  }

}
