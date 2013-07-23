def get_1stcic(fpga, subband, pol, reim):
    first_cic = np.fromstring(fpga.snapshot_get('s'+str(subband)+'_p'+str(pol)+reim+'_firstcic', man_trig=True, man_valid=True)['data'],dtype='<i4')
    first_cic_full = np.fromstring(fpga.snapshot_get('s'+str(subband)+'_p'+str(pol)+reim+'_firstcic_full', man_trig=True, man_valid=True)['data'],dtype='<i8')
    return first_cic, first_cic_full

def get_dr16(fpga, subband, pol, reim):
    dr16 = np.fromstring(fpga.snapshot_get('s'+str(subband)+'_p'+str(pol)+reim+'_dr16', man_trig=True, man_valid=True)['data'], dtype='<i8')
    return dr16

def get_halfband(fpga, subband, pol, reim):
    halfband = np.fromstring(fpga.snapshot_get('s'+str(subband)+'_p'+str(pol)+reim+'_halfband', man_trig=True, man_valid=True)['data'], dtype='<i8')
    return halfband

def get_chc(fpga, subband, pol, reim):
    chc = np.fromstring(fpga.snapshot_get('cic'+str(pol)+reim+'_snap', man_trig=True, man_valid=True)['data'], dtype='<i4')
    return chc

def plotfft(data, lo_f, bw, dec_rate):
    f_index = np.linspace(lo_f - bw/(2.*dec_rate), lo_f + bw/(2.*dec_rate), len(data))
    plot(f_index, 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(data)))))

def plot_dr16(fpga, subband, lo_f, bw, dec_rate):
    dr16_p1_re = get_dr16(fpga, subband, 1, 're')
    dr16_p1_im = get_dr16(fpga, subband, 1, 'im')
    dr16_p2_re = get_dr16(fpga, subband, 2, 're')
    dr16_p2_im = get_dr16(fpga, subband, 2, 'im')
    dr16_p1_len = len(dr16_p1_re)
    dr16_p1 = np.zeros(dr16_p1_len, dtype=np.complex64)
    dr16_p1.real = dr16_p1_re.astype(np.float)
    dr16_p1.imag = dr16_p1_im.astype(np.float)
    subplot(211)
    plotfft(dr16_p1, lo_f, bw, dec_rate)
    dr16_p2_len = len(dr16_p2_re)
    dr16_p2 = np.zeros(dr16_p2_len, dtype=np.complex64)
    dr16_p2.real = dr16_p2_re.astype(np.float)
    dr16_p2.imag = dr16_p2_im.astype(np.float)
    subplot(212)
    plotfft(dr16_p2, lo_f, bw, dec_rate)

def plot_1stcic(fpga, subband, lo_f, bw, dec_rate):
    c_p1re, c_p1re_full = get_1stcic(fpga, subband, 1, 're')
    c_p1im, c_p1im_full = get_1stcic(fpga, subband, 1, 'im')
    c_p2re, c_p2re_full = get_1stcic(fpga, subband, 2, 're')
    c_p2im, c_p2im_full = get_1stcic(fpga, subband, 2, 'im')
    figure()
    c_p1_len = len(c_p1re)
    c_p1 = np.zeros(c_p1_len, dtype=np.complex64)
    c_p1.real = c_p1re.astype(np.float)
    c_p1.imag = c_p1im.astype(np.float)
    subplot(211)
    plotfft(c_p1, lo_f, bw, dec_rate)
    c_p2_len = len(c_p2re)
    c_p2 = np.zeros(c_p2_len, dtype=np.complex64)
    c_p2.real = c_p2re.astype(np.float)
    c_p2.imag = c_p2im.astype(np.float)
    subplot(212)
    plotfft(c_p2, lo_f, bw, dec_rate)
    figure()
    c_p1f_len = len(c_p1re_full)
    c_p1f = np.zeros(c_p1f_len, dtype=np.complex64)
    c_p1f.real = c_p1re_full.astype(np.float)
    c_p1f.imag = c_p1im_full.astype(np.float)
    subplot(211)
    plotfft(c_p1f, lo_f, bw, dec_rate)
    c_p2f_len = len(c_p2re_full)
    c_p2f = np.zeros(c_p2f_len, dtype=np.complex64)
    c_p2f.real = c_p2re_full.astype(np.float)
    c_p2f.imag = c_p2im_full.astype(np.float)
    subplot(212)
    plotfft(c_p2f, lo_f, bw, dec_rate)

def plot_hb(fpga, subband, lo_f, bw, dec_rate):
    hb_p1re = get_halfband(fpga, subband, 1, 're')
    hb_p1im = get_halfband(fpga, subband, 1, 'im')
    hb_p2re = get_halfband(fpga, subband, 2, 're')
    hb_p2im = get_halfband(fpga, subband, 2, 'im')
    hb_p1_len = len(hb_p1re)
    hb_p1 = np.zeros(hb_p1_len, dtype=np.complex64)
    hb_p1.real = hb_p1re.astype(np.float)
    hb_p1.imag = hb_p1im.astype(np.float)
    subplot(211)
    plotfft(hb_p1, lo_f, bw, dec_rate)
    hb_p2_len = len(hb_p2re)
    hb_p2 = np.zeros(hb_p2_len, dtype=np.complex64)
    hb_p2.real = hb_p2re.astype(np.float)
    hb_p2.imag = hb_p2im.astype(np.float)
    subplot(212)
    plotfft(hb_p2, lo_f, bw, dec_rate)


def plot_chc(fpga, subband):
    chc_p1re = get_chc(fpga, subband, 1, 're')
    chc_p1im = get_chc(fpga, subband, 1, 'im')
    chc_p2re = get_chc(fpga, subband, 2, 're')
    chc_p2im = get_chc(fpga, subband, 2, 'im')
    chc_p1_len = len(chc_p1re)
    chc_p1 = np.zeros(chc_p1_len, dtype=np.complex64)
    chc_p1.real = chc_p1re.astype(np.float)
    chc_p1.imag = chc_p1im.astype(np.float)
    subplot(211)
    plotfft(chc_p1, lo_f, bw, dec_rate)
    chc_p2_len = len(chc_p2re)
    chc_p2 = np.zeros(chc_p2_len, dtype=np.complex64)
    chc_p2.real = chc_p2re.astype(np.float)
    chc_p2.imag = chc_p2im.astype(np.float)
    subplot(212)
    plotfft(chc_p2, lo_f, bw, dec_rate)
    

