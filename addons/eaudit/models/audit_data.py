from odoo import models, fields, api


class eaudit(models.Model):
    _name = 'eaudit.auditdata'
    _description = 'Model Audit Data'

    nama = fields.Char(String='No LHP', required=True)
    tahun = fields.Date(String='Tahun Audit', required=True)
    tgl = fields.Date(String='Tanggal LHP', required=True)
    temuan = fields.Text(String='Temuan', required=True)
    penyebab = fields.Text(String='Penyebab', required=True)
    rekomendasi = fields.Text(String='Rekomendasi', required=True)