import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../company.service';
import { Company } from '../models/company.interface';
import { Vacancy } from '../models/vacancy.interface';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrl: './company-list.component.css'
})

export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  selectedCompanyId: number | null = null;
  vacancies: Vacancy[] = [];
  
  constructor (private companyService: CompanyService) {}

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies(): void {
    this.companyService.getCompanies().subscribe((companies: Company[]) => {
      this.companies = companies
    })
  }

  selectCompany(companyId: number): void {
    this.selectedCompanyId = companyId;
    this.getVacanciesForSelectedCompany();
  }

  getVacanciesForSelectedCompany(): void {
    if (this.selectedCompanyId != null) {
      this.companyService.getVacancies(this.selectedCompanyId).subscribe((vacancies: Vacancy[]) => {
        this.vacancies = vacancies;
      })
    }
  }
}

