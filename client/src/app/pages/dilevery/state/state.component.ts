import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-state',
  templateUrl: './state.component.html',
  styleUrls: ['./state.component.css']
})
export class StateComponent implements OnInit {
  state!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.state!! = new FormGroup({
      'State_id':new FormControl(null, Validators.required),
      'State_name':new FormControl(null, Validators.required),
    });
  }
  get State_id() {
    return this.state!.get('State_id');
  }
  get State_name() {
    return this.state!.get('State_name');
  }

}
