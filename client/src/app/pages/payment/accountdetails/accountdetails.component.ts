import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-accountdetails',
  templateUrl: './accountdetails.component.html',
  styleUrls: ['./accountdetails.component.css']
})
export class AccountdetailsComponent implements OnInit {
  acdet!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.acdet! = new FormGroup({
      'acc_holder_name':new FormControl(null, Validators.required),
      'bank':new FormControl(null, Validators.required),
      'branch':new FormControl(null, Validators.required),
      'account_no':new FormControl(null, Validators.required),
      'ifsc_code':new FormControl(null, Validators.required),
      
      
      
      
    });
  }
  get acc_holder_name() {
    return this.acdet!.get('acc_holder_name');
  }
  get bank() {
    return this.acdet!.get('bank');
  }
  get branch() {
    return this.acdet!.get('branch');
  }
  get account_no() {
    return this.acdet!.get('account_no');
  }
  get ifsc_code() {
    return this.acdet!.get('ifsc_code');
  }
  
  

}
