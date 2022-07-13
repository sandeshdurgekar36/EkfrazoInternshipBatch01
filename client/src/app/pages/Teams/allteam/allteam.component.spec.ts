import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllteamComponent } from './allteam.component';

describe('AllteamComponent', () => {
  let component: AllteamComponent;
  let fixture: ComponentFixture<AllteamComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AllteamComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AllteamComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
