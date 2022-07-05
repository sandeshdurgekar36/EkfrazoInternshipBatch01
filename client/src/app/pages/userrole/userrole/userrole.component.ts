import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-userrole',
  templateUrl: './userrole.component.html',
  styleUrls: ['./userrole.component.css']
})
export class UserroleComponent implements OnInit {
  userrole!:FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.userrole! = new FormGroup({
      'User_Role_Name':new FormControl(null, Validators.required),
            
    });
  }
  get User_Role_Name() {
    return this.userrole!.get('User_Role_Name');
  }
  

}
