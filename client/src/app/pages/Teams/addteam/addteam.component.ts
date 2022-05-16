import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-addteam',
  templateUrl: './addteam.component.html',
  styleUrls: ['./addteam.component.css']
})
export class AddteamComponent implements OnInit {
  adteam!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.adteam! = new FormGroup({
      'username':new FormControl(null, Validators.required),
      'password':new FormControl(null, Validators.required),
      'email' : new FormControl(null, [Validators.required, Validators.email]),
      'phone' : new FormControl(
        null,
        [
          Validators.required,
          Validators.pattern('^\\s*(?:\\+?(\\d{1,3}))?[-. (]*(\\d{3})[-. )]*(\\d{3})[-. ]*(\\d{4})(?: *x(\\d+))?\\s*$')
        ]),
      'srole':new FormControl(null, Validators.required),
    });  
  }
  get username() {
    return this.adteam!.get('username');
  }
  get password() {
    return this.adteam!.get('password');
  }
  get email() {
    return this.adteam!.get('email');
  }
  get phone() {
    return this.adteam!.get('phone');
  }
  get srole() {
    return this.adteam!.get('srole');
  }

}
