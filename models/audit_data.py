from odoo import models, fields, api

class eaudit(models.Model):
    _name = 'eaudit.auditdata'
    _description = 'Model Audit Data'

    name = fields.Char(String='No LHP', required=True)
    tahun = fields.Integer(String='Tahun Audit', required=True)
    tgl = fields.Date(String='Tanggal LHP', required=True)
    temuan = fields.Text(String='Temuan', required=True)
    penyebab = fields.Text(String='Penyebab', required=True)
    rekomendasi = fields.Text(String='Rekomendasi', required=True)

    jt_administratif = fields.Text(String='Administratif', required=True)
    jt_material = fields.Text(String='Material', required=True)

    tl_pic = fields.Text(String='PIC', required=True)
    tl_desk = fields.Text(String='Deskripsi', required=True)
    tl_bukti_file = fields.Binary(String='File Bukti', attachment=True, required=True)
    tl_bukti_name = fields.Char(String='Nama File Bukti', required=True)

    status = fields.Selection([('Open', 'Open'), ('Close', 'Close')], string='Status', required=True)
    saldo = fields.Float(String='Saldo', required=True)

    verifikasi = fields.Selection([('Sudah', 'Sudah'), ('Belum', 'Belum')], string="Verifikasi", required=True)