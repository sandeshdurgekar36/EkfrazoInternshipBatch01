import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router'; 
import { UserroleService } from 'src/app/services/userrole.service'; '../services/userrole.service';

@Component({
  selector: 'app-masterpage',
  templateUrl: './masterpage.component.html',
  styleUrls: ['./masterpage.component.css']
})
export class MasterpageComponent implements OnInit {
  
  

  constructor(private uService: UserroleService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.userroleform = new FormGroup({
      'User_Role_Name':new FormControl(null, Validators.required)
    }); 
 
  }
  get User_Role_Name() {
    return this.userroleform.get('User_Role_Name');
  }
  
  userroleform = this.fb.group({
    User_Role_Name : ['',Validators.required],
   })
   lusers(){ 
    console.log(this.userroleform.value)
    this.uService.lusers(this.userroleform.value).subscribe(response =>{
      alert("User Role Name added");
    })
  }
  
}
