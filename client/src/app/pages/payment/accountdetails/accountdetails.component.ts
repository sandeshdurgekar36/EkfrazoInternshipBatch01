import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { AccountService } from 'src/app/services/account.service'; 
import { Router } from '@angular/router';


@Component({
  selector: 'app-accountdetails',
  templateUrl: './accountdetails.component.html',
  styleUrls: ['./accountdetails.component.css']
})
export class AccountdetailsComponent implements OnInit {
  

  constructor(private aService: AccountService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.acdetform = new FormGroup({
      'acc_holder_name':new FormControl(null, Validators.required),
      'bank':new FormControl(null, Validators.required),
      'branch':new FormControl(null, Validators.required),
      'account_no':new FormControl(null, Validators.required),
      'ifsc_code':new FormControl(null, Validators.required),
    });
  }
  get acc_holder_name() {
    return this.acdetform.get('acc_holder_name');
  }
  get bank() {
    return this.acdetform.get('bank');
  }
  get branch() {
    return this.acdetform.get('branch');
  }
  get account_no() {
    return this.acdetform.get('account_no');
  }
  get ifsc_code() {
    return this.acdetform.get('ifsc_code');
  }
  acdetform = this.fb.group({
    acc_holder_name: ['',Validators.required],
    bank: ['',Validators.required],
    branch: ['',Validators.required],
    account_no: ['',Validators.required],
    ifsc_code: ['',Validators.required],
  })
  accounts(){
    console.log(this.acdetform.value)
    this.aService.accounts(this.acdetform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}